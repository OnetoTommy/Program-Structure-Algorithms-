import java.util.Stack;

public class HW1_Q3 {

    public static void main(String[] args) {
    String string = "I { love [ the {rains ] ()";
    boolean isCorrespond = isParenthesis(string);
    System.out.println("The output is " + isCorrespond);
  }

  public static boolean isParenthesis(String string){
    Stack<Character> queue = new Stack<>();
    for(char character : string.toCharArray()){
      if (character == '{' || character == '(' || character == '[') {
        queue.push(character);
      }
      else if(character == '}' || character == ')' || character == ']'){
        if (queue.isEmpty()) {
          return false;
        }

        char left = queue.pop();
        if (!isMatch(left, character)) {
          return false;
        }
      }
    }
    return queue.isEmpty();
  }

  public static boolean isMatch(char left, char right){
    return (
      (left == '(' && right ==')')||
      (left == '{' && right == '}') ||
      (left == '[' && right == ']')) ;
  }
}