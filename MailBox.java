public class MailBox
{
   private String[] messages;
   private String[] keepedMessages;
   private int numberOfMessages;
   private String greeting;
   private String passcode;
   
   MailBox()
   {
      messages = new String[5];
      keepedMessages = new String[5];
      numberOfMessages = -1;  
      passcode = "password";
      greeting = "Hello, leave a message";
   }
   
   public String getMessage(int num)
   {
      return messages[num];
   }
   
   public void sendMessage(String str)
   {
      numberOfMessages++;
      messages[numberOfMessages] = str;
   }
   
   public void setGreeting(String str)
   {
      greeting = str;
   }
   
   public void setPasscode(String pass)
   {
      passcode = pass;
   }
   
   public void deleteMessage(int num)
   {
      messages[num] = "";
   }
   
   public void keepMessage(int num)
   {
     keepedMessages[num] = messages[num];
   }
   
   public String getGreeting()
   {
      return greeting;
   }
   public String getPasscode()
   {
      return passcode;
   }
}