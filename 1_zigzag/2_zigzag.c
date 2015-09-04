#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned int uint;


char* convert(char* s, int numRows)
{
    if ( 1 == numRows)
    {
        return s;
    }
    char* ret;
    uint len = strlen(s);
    ret = (char*)malloc(sizeof(s)*len);
    uint ind = 0;
    for (int i=0; i< numRows; i++)
    {
        if ( 0 == i )
        {
            for (int j=0; j*(2*numRows-2) < len; j++)
            {
                ret[ind]=s[j*(2*numRows-2)];
                ind += 1;
            }
        }
        else if (numRows - 1 == i){
            for (int j=0; i+j*(2*numRows-2) < len; j++)
            {
                ret[ind]=s[i+j*(2*numRows-2)];
                ind += 1;
            }
        }
        else
        {
            for (int j = 0; (i+j*2*(numRows-2) < len) || (i + j*2*(numRows - i) < len); j++)
            {
                if (j/2.0 == 0)
                {
                    ret[ind] = s[i + j*(2*numRows - 2)];
//                    printf("even ret[%d] is %c\n", ind,ret[ind]);
                    ind += 1;
                }
                else
                {
                    ret[ind] = s[i + j*2*(numRows - i-1)];
//                    printf("odd ret[%d] is %c\n", ind,ret[ind]);
                    ind += 1;
                }
            }
        }
    }
//    printf("s is %s\n",s);
//    printf("ret  is %s\n",ret);
//    printf("true is PAHNAPLSIIGYIR\n");
    return ret;
}

int main(void)
{
    char* s = "PAYPALISHIRING";   
    uint len = strlen(s);
    char* ret;
    ret = (char*)malloc(sizeof(s)*len);
    
    ret = convert(s,3);

    printf("%s\n",ret);

    return 0;
}
