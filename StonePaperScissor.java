import java.util.*;
class StonePaperScissor

{
    int round;
    int pointplayer;
    int pointcomputer;
    String p;
    String c;
    StonePaperScissor()
     {
         round=1;
         pointplayer=0;
         pointcomputer =0;
         p="";
         c="";
        }
    void input()
    {
        
        System.out.println("Hello Player ");
        System.out.println("Ready for round "+round);
        round++;
        System.out.println("Please enter 1,2 and 3 respectively");
        
        
    }
    void play()
    {
        
        Scanner sc =new Scanner(System.in);
        int player = sc.nextInt();
        if(player==1)
        {
            p="STONE";
        }
        else if(player==2)
        {
            p="PAPER";
        }
         else if(player==3)
        {
            p="SCISSOR";
        }
        System.out.println(p+" is your choise");
        double st= Math.random();
        st=st*3;
        if(st<=1)
        {
            c="STONE";
        }
        
        if((st>1)&&(st<=2))
        {
           c="PAPER";
        }
        if((st>2)&&(st<=3))
        {
            c="SCISSOR";

        }
        System.out.println(c+" Computer choise");

        
    }
    
    void point()
    { 
        
        if(p.equals(c) )
        {
         pointplayer ++;
         pointcomputer ++;
        }
        if(p=="STONE"&&c=="SCISSOR")
        {pointplayer ++;
        }
        if(p=="PAPER"&&c=="STONE")
        {pointplayer ++;
        }
        if(p=="SCISSOR"&&c=="PAPER")
        {pointplayer ++;
        }
        
        if(c=="STONE"&&p=="SCISSOR")
        { pointcomputer ++;
        }
        if(c=="PAPER"&&p=="STONE")
        { pointcomputer ++;
        }
        if(c=="SCISSOR"&&p=="PAPER")
        { pointcomputer ++;
        }
        
        
    }
    void calculation()
    {
        System.out.println("Total points");
         System.out.println("Player "+pointplayer);System.out.println("Computer "+pointcomputer);
         
       
        if(pointplayer>pointcomputer)
        {
            System.out.println("You Win");
            
        }
        else if(pointplayer<pointcomputer)
        {
            System.out.println("You Lose");
           
        }
        else
        {
            System.out.println("Draw");
        }
    }
    
    public static void main()
    {
        System.out.println("Instructions ");
        System.out.println("Enter 1 for stone,Enter 2 for paper and 3 for scissor ");
          System.out.println("Please Enter number of rounds  ");
          Scanner sc =new Scanner(System.in);
          int r= sc.nextInt();
       StonePaperScissor ob =new StonePaperScissor();
       for(int i=1;i<=r;i++){
       ob.input();
       ob.play();
       ob.point();
    
       }
        
        ob.calculation();
    
    }
}