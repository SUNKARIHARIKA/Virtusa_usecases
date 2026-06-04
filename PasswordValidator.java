//Password Validator
import java.util.*;
public class PasswordValidator {
    boolean length_valid(String password){
        int length=password.length();
        if (length<8)
            return false;
        else
            return true;
    }
    boolean uppercase_valid(String password){
        for(int i=0;i<password.length();i++){
            char ch=password.charAt(i);
            if(Character.isUpperCase(ch)){
                return true;
            }
        }
        return false;
    }
    boolean digit_valid(String password){
        for(int i=0;i<password.length();i++){
            char ch=password.charAt(i);
            if(Character.isDigit(ch)){
                return true;
            }
        }
        return false;
    }
    String check(String password){
        String feedback="";
        Boolean result1=length_valid(password);
        if (!(result1))
            feedback+="Password length is too short\n";
        Boolean result2=uppercase_valid(password);
        if (!(result2))
            feedback+="No uppercase letter in password\n";
        Boolean result3=digit_valid(password);
        if (!(result3))
            feedback+="No digits in password";
        if(result1 && result2 && result3)
            feedback="0";
        return feedback;
    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        PasswordValidator pv=new PasswordValidator();
        System.out.println("enter the password");
        String password=sc.nextLine();
        String result=pv.check(password);
        if (result.equals("0")){
            System.out.println("password is standard and secure");
        }
        else{
            while(!result.equals("0")){
                System.out.println(result);
                System.out.println("enter the password again");
                String password1=sc.nextLine();
                result=pv.check(password1);

            }
            System.out.println("password is standard and secure");
        }
        }
    }
