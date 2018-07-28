package Argu;

public class Args {
 

  public static  void main(String[] args) {
    int i,s=0,len;
    len=args.length;
    System.out.println("len="+len);
    for(i=0;i<len;i++)
   {
     System.out.println(""+(args[i]));
     s++;
   }
   
   System.out.println("s="+s);
  }
}
