import java.util.ArrayDeque;
import java.util.Deque;

public class HW1_Q3_Queue {
  public static void main(String[] args) {
    String string = "I { love [ the {rains}()]}";
    boolean isCorrespond = addParenthesis(string);
    System.out.println("The output is " + isCorrespond);
  }

  public static boolean addParenthesis(String string) {
    Deque<Character> queue = new ArrayDeque<>();
    for (char character : string.toCharArray()) {
      if (character == '{' || character == '(' || character == '[') {
        queue.addLast(character);
      } else if (character == '}' || character == ')' || character == ']') {

        if (queue.isEmpty()) {
          return false;
        }
        char open = queue.pollLast();
        if (!match(open, character)) {
          return false;
        }
      }
    }
    return true;
  }

  public static boolean match(char open, char close) {
    return ((open == '(' && close == ')') ||
        (open == '{' && close == '}') ||
        (open == '[' && close == ']'));
  }
}
