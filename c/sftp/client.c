/* networking hw -- sftp client
 * 
 * client.c
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
#include <netdb.h>

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[])
{
    if (argc < 5) {
       fprintf(stderr, "usage: %s <input_filename> <output_filename> <server_ip_address> <server_port#>\n", argv[0]);
       exit(1);
    }

    int clientfd, portno;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char buffer[10];
    int out_filename_len;

    // init vars
    out_filename_len = strlen(argv[2]);
    server = gethostbyname(argv[3]);
    if (server == NULL) {
        error("ERROR, no such host\n");
    }
    portno = atoi(argv[4]);

    // create client socket
    clientfd = socket(AF_INET, SOCK_STREAM, 0);
    if (clientfd < 0)
        error("ERROR opening socket");

    // connect to server socket
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(portno);
    if (connect(clientfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0)
        error("ERROR connecting server socket");

    // send the length of output filename
    if (write(clientfd, &out_filename_len, sizeof(out_filename_len)) < 0) {
         error("ERROR writing out_filename_len to socket");
    }

    // send output filename
    if (write(clientfd, argv[2], out_filename_len) < 0) {
         error("ERROR writing out_filename to socket");
    }

    // open file
    int filefd = open(argv[1], O_RDONLY);
    if (filefd < 0) {
         printf("ERROR open file %s", argv[1]);
    }

    int count = 0;
    // keep reading file and send buffer in chunks of 10 bytes till count is less than 10 bytes (last few bytes)
    do {
        count = read(filefd, buffer, 10);
        if (count > 0) {
            if (write(clientfd, buffer, count) < 0) {
                 error("ERROR writing buffer to socket");
            }
        }
        bzero(buffer,10);
    }
    while (count == 10);

    close(clientfd);

    exit(0);
}
