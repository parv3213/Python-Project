//IMPORT SCANNER FUNCTION
import java.util.Scanner; 

public class project{
    public static void main(String args[])
    {   
        start();
        //Creating an object of Scanner class
        Scanner userInput= new Scanner(System.in);
        
        //LOOP IS REQUIRED TO RESTART THE PROGRAM
        while(true)
        {
            System.out.print("Press 1 for one more time:\n");
            int d=userInput.nextInt();
            if(d==1)
            {
                start();
            }
            else{
                return;
            }
       }

    }

    public static void start()
    {
        Scanner userInput= new Scanner(System.in);
        System.out.println("\nWelcome to Stone Paper Scissors\n");
        System.out.print("Enter the Name of Player 1:");
        String player1= userInput.nextLine();
        System.out.print("Enter the Name of Player 2:");
        String player2= userInput.nextLine();
        System.out.print("Enter the number of times you guys want to repeat:");
        int n= userInput.nextInt();
        int i=1;
        int num1=0,num2=0,num3=0;
        //System.out.println(ran());
        for (i=1;i<=n;i++){   
            int rand1=ran();
            int rand2=ran();
            
            int winner= win(rand1,rand2);
            if (winner ==1){
                num1+=1;
            }
            else if (winner==2){
                num2+=1;
            }
            else
            {
                num3+=1;
            }
            display(i,winner,player1,player2);
            promptEnterKey();
           }
           System.out.println("\n \nNumber of Repeat:\t"+n+"\n"+"Number of times "+player1+" wins:\t"+num1
           +"\n"+"Number of times "+player2+" wins:\t"+num2+"\n"+"Number of Draws:\t"+num3+"\n\n");
           if(num1>num2)
           {
               System.out.println(player1+" is the Winner");
           }
           else if(num2>num1)
           {
            System.out.println(player2+" is the Winner");
           }
           else{
            System.out.println("It is a Tie!");
           }



    }
            //Random function
            public static int ran(){
                int x = (int)(Math.random()*((3-1)+1))+1;
                return x;
            }
            //winner function
            public static int win(int x,int y){
                //1=Stone, 2=Paper, 3=Scissors
                if (x==1 && y==2)
                {
                    return 2;
                }
                else if  (x==1 && y==1)
                {
                    return 0;
                }
                else if  (x==1 && y==3)
                {
                    return 1;
                }
                //x=2
                else if  (x==2 && y==1)
                {
                    return 1;
                }
                else if  (x==2 && y==2)
                {
                    return 0;
                }
                else if  (x==2 && y==3)
                {
                    return 2;
                }
                //x=3
                else if  (x==3 && y==1)
                {
                    return 2;
                }
                else if  (x==3 && y==2)
                {
                    return 1;
                }
                else if  (x==3 && y==3)
                {
                    return 0;
                }
                else
                {
                    return 4;
                }

            }

            //Display function
            public static void display(int n,int x, String a,String b)
            {
                System.out.println();
                if (x==1)
                {
                    System.out.print("WINNER OF "+n+" is:\t");
                    System.out.println(a);
                }
                else if (x==2)
                {
                    System.out.print("WINNER OF "+n+" is:\t");
                    System.out.println(b);
                }
                else if (x==4)
                {
                    System.out.println("OOPS ERROR!");
                }
                else{
                    System.out.println("WINNER OF "+n+" is:\tDRAW!");
                }
            }
            public static void promptEnterKey(){
                System.out.println("Press \"ENTER\" to continue...");
                Scanner scanner = new Scanner(System.in);
                scanner.nextLine();
             }

}