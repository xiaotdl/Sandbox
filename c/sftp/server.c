/* networking hw -- sftp server
 * 
 * server.c
 *
 * Author: Wendi Weng
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
     if (argc < 2) {
         fprintf(stderr,"usage: %s <server_port>\n", argv[0]);
         exit(1);
     }

     int serverfd, connfd, portno;
     struct sockaddr_in serv_addr, cli_addr;
     socklen_t clilen;
     char buffer[5];
     int out_filename_len;
     char out_filename[1024];

     // create server socket
     serverfd = socket(AF_INET, SOCK_STREAM, 0);
     if (serverfd < 0)
        error("ERROR opening socket");

     // bind socket
     portno = atoi(argv[1]);
     bzero((char *) &serv_addr, sizeof(serv_addr));
     serv_addr.sin_family = AF_INET;
     serv_addr.sin_addr.s_addr = INADDR_ANY;
     serv_addr.sin_port = htons(portno);
     if (bind(serverfd, (struct sockaddr *) &serv_addr,
              sizeof(serv_addr)) < 0)
              error("ERROR on binding");

     // socket starts in listen mode
     listen(serverfd, 5);
     clilen = sizeof(cli_addr);
     while (1) {
         // accept connected client socket
         printf("+---------waiting to accept client connection---------+\n");
         connfd = accept(serverfd,
                         (struct sockaddr *) &cli_addr,
                         &clilen);
         if (connfd < 0)
              error("ERROR on accept");
         printf("client socket connected, starting to receive file...\n");

         // receive the output filename length
         if (read(connfd, &out_filename_len, sizeof(out_filename_len)) < 0) {
            error("ERROR reading out_filename_len");
         };
         printf("received out_filename_len: %d\n", out_filename_len);

         // receive the output filename
         bzero(out_filename, 1024);
         if (read(connfd, out_filename, out_filename_len) < 0) {
            error("ERROR reading out_filename");
         };
         printf("received out_filename: %s\n", out_filename);

         // open output file for writing
         int filefd = open(out_filename, O_WRONLY|O_CREAT, 0664);
         if (filefd < 0) {
             error("ERROR openning file");
         }

         int count = 0;
         while ((count = read(connfd, buffer, 5)) > 0) {
             /*printf("[debug] count %d\n", count);*/
             /*printf("[debug] buffer: '%s'\n", buffer);*/
             write(filefd, buffer, count);
             bzero(buffer, 5);
         }
         close(filefd);
         printf("received file successfully!\n");

        close(connfd);
     }
     close(serverfd);
     return 0;
}
