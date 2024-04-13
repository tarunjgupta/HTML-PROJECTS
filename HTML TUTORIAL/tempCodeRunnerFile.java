import java.io.*;
class Solution
 {
    public int strStr(String haystack, String needle) 
    {
        int i,f=0;
        char ch;
        String s1="";
        for(i=0;i<haystack.length();i++)
        {
            ch=haystack.charAt(i);
            if(ch!=' ')
            s1=s1+ch;
            if(s1.length()==needle.length())
            {
                if(s1==needle)
                {
                f=1;
                break;
                }
                else
                {
                    i=i-s1.length();
                    s1="";
                }
            }
        }
        if(f==1)
        return (i+1-needle.length());
        else
        return -1;
    }
}
public static void main(String arg[])throws Exception
{
int res;
String haystack,needle;
DataInputStream in=new DataInputStream(System.in);
System.out.println("Enter the Haystack: ");
haystack=in.readLine();
System.out.println("Enter the needle: ");
needle=in.readLine();
Solution obj=new Solution();
res=obj.strStr(haystack,needle);
System.out.println(res);
}