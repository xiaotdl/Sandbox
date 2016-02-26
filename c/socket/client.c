/*
* This is a client socket.
*/
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h> 


int main(int argc, char *argv[])
{
    int sockfd = 0, n = 0;
    char recvBuff[1024];
    struct sockaddr_in serv_addr; 

    if (argc != 2) {
        printf("\n Usage: %s <server ip>\n", argv[0]);
        return 1;
    }

    memset(recvBuff, '0', sizeof(recvBuff));
    if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("\n Error: Could not create socket.\n");
        return 1;
    }

    memset(&serv_addr, '0', sizeof(serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(5000);

    if (inet_pton(AF_INET, argv[1], &serv_addr.sin_addr) <= 0) {
        printf("\n inet_pton error.\n");
        return 1;
    }

    // connect() connects to the server ip and port
    if (connect(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
        printf("\n Error: Connection failed.\n");
        return 1;
    }

    while ((n = read(sockfd, recvBuff, sizeof(recvBuff) - 1)) > 0) {
        recvBuff[n] = 0;
        if (fputs(recvBuff, stdout) == EOF) {
            printf("\n Error: Fputs error.\n");
        }
    }

    if (n < 0) {
        printf("\n Read error.\n");
    }

    return 0;
}
