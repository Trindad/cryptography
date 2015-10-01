#include <sys/socket.h>
#include <netinet/in.h>
#include <stdio.h>
#include <strings.h>
#include <string.h>
#include <unistd.h>


static char mesg[100];
static char response[100];

void (*pointer_to_function)();
void one_function() {
    sprintf(response, "Voce enviou: %s\n", mesg);
}

void other_function() {
    sprintf(response, "Parabens, voce concluiu o trabalho!!!");
}

int main(int argc, char**argv)
{
    pointer_to_function = &one_function;
    int sockfd,n;
    struct sockaddr_in servaddr,cliaddr;
    socklen_t len;

    sockfd=socket(AF_INET,SOCK_DGRAM,0);

    bzero(&servaddr,sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr=htonl(INADDR_ANY);
    servaddr.sin_port=htons(32000);
    bind(sockfd,(struct sockaddr *)&servaddr,sizeof(servaddr));

    for (;;)
    {
        len = sizeof(cliaddr);
        n = recvfrom(sockfd,mesg,1000,0,(struct sockaddr *)&cliaddr,&len);

        mesg[n] = 0;
        printf(">>%s<<\n", mesg);
        pointer_to_function();
        n = strlen(response);

        sendto(sockfd,response,n,0,(struct sockaddr *)&cliaddr,sizeof(cliaddr));
    }
}