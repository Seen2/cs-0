package work;

import java.util.Scanner;



class homo{
  String man;
  void sman(){
    System.out.println("man is "+man); 
  }
}
class monk extends homo{
 String bandar;
 void showmb(){
   System.out.println("man= "+man+" bandar= "+bandar); 
 } 
}

public class Ex1 {

  public static void main(String[] args) {
    String S;
    String s;
    System.out.println("who is man");
    Scanner sc=new Scanner(System.in);
    S=sc.nextLine();
    System.out.println("who is monkey");
    s=sc.nextLine();  
    homo superOb=new homo();
    monk subOb=new monk();
    superOb.man=S;
    subOb.bandar=s;
    subOb.man=S;
    superOb.sman();
    subOb.sman();
    subOb.showmb();
   
  }
}
