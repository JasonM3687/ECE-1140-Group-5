import java.util.Scanner;

public class main
{
   public static void main(String []args)
   {
      //leave message
      //retreave a message
      
      Scanner read = new Scanner(System.in);
      
      MailBox mailBox = new MailBox();
      Telephone A = new Telephone(mailBox);
      
      int num2 = 0;
      
      while(num2 == 0)
      {
         System.out.println("Hint: default Passcode = password");
         System.out.println("Please Enter Passcode");
         String pass = read.nextLine();
         if(pass.compareTo(A.getPasscode()) == 0)
         {
            System.out.println("Do you want to send a message, read a message, set a greeting, or change the passcode");
            System.out.println("Enter 1 for send a message or 2 for read a message 3 for setting a greeting or 4 for setting a passcode");
            int num = read.nextInt();
            
            if(num == 1)
            {
               //sending a message
               System.out.println("Type the message you want to send");
               String str = read.nextLine();
               A.sendMessage(str);
               System.out.println("Your message is sent");
            }
            
            if(num == 2)
            {
               //reading a message
               System.out.println("What message do you want to read, enter number 1-5");
               int num1 = read.nextInt();
               System.out.println("your message is");
               System.out.println(A.retrieveMessage(num1));
               System.out.println("Do you want to keep or delete message 1 or 2");
               int num3 = read.nextInt();
               if(num3 == 1)
               {
                  //delete
                  A.deleteMessage(num1);
               }
               
               if(num3 == 2)
               {
                  //keep
                  A.keepMessage(num1);
               }
            }
            
            if(num == 3)
            {
               //setting a greeting
               System.out.println("Your current greeting is " + A.getGreeting());
               System.out.println("Enter your new greeting");
               String str1 = read.nextLine();
               A.setGreeting(str1);
               System.out.println("Your new greeting is " + str1);
            }
            
            if(num == 4)
            {
               //setting a passcode
               System.out.println("What message do you want to read, enter number 1-5");
               int num5 = read.nextInt();
               System.out.println("your message is " + A.retrieveMessage(num5));
            }
            
            System.out.println("Do you want to complete more actions? 1 yes");
            int num6 = read.nextInt();
            if(num6 == 1)
            { 
               num2++;
            }
         }
         else
         {
           System.out.println("Incorrect Passcode try again");
         }
      }
   }
}
