/*
* This is a server socket.
*/
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h> 


int main(int argc, char *argv[]) {
    int listenfd = 0, connfd = 0;
    struct sockaddr_in serv_addr;
    float interval = 0.1;

    char sendBuff[1025];
    time_t ticks;

    // socket() creates a socket in kernel and returns a socket descriptor
    // AF_INET means IPv4
    // SOCK_STREAM means TCP
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    memset(&serv_addr, '0', sizeof(serv_addr));
    memset(sendBuff, '0', sizeof(sendBuff));
    
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY); // host to network long
    serv_addr.sin_port = htons(5000);              // host to network short

    // binds the serv_addr info to the socket created
    bind(listenfd, (struct sockaddr*) &serv_addr, sizeof(serv_addr));

    // starts listening, '10' specifies the max client connections
    listen(listenfd, 10);

    // wait till the client socket connected
    while (1) {
        // accept() will complete the TCP connection and returns client socket
        connfd = accept(listenfd, (struct sockaddr*) NULL, NULL);

        ticks = time(NULL);
        snprintf(sendBuff, sizeof(sendBuff), "%.24s\r\r", ctime(&ticks));
        // write() sends response to the client socket
        write(connfd, sendBuff, strlen(sendBuff));

        close(connfd);
        sleep(interval);
    }

    return 0;
}
