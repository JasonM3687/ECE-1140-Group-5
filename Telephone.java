public class Telephone
{
   private MailBox mail = new MailBox();
   
   Telephone(MailBox m)
   {
      mail = m;
   }
   
   public void sendMessage(String msg)
   {
      mail.sendMessage(msg);
   }
   
   public String retrieveMessage(int num)
   {
      return mail.getMessage(num);
   }
   
   public void setGreeting(String str)
   {
      mail.setGreeting(str);
   }
   
   public void setPasscode(String str)
   {
      mail.setPasscode(str);
   }
   
   public void deleteMessage(int messageID)
   {
      mail.deleteMessage(messageID);
   }
   
   public void keepMessage(int messageID)
   {
      mail.keepMessage(messageID);
   }
   
   public String getGreeting()
   {
      return mail.getGreeting();
   }
   
   public String getPasscode()
   {
      return mail.getPasscode();
   }
}
