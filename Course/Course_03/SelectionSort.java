package Course.Course_03;

public class SelectionSort {

  public static void main(String[] args) {
    int[] array = { 10, 7, 8, 9, 1, 5 };
    System.out.println("Original Array:");
    printArray(array);

    selectionSort(array);

    System.out.println("Select Array:");
    printArray(array);
  }

  public static int[] selectionSort(int[] array) {

    int index = 0;
    int len = array.length;
    while (index < len - 1) {
      int min = array[index];
      int k = index;
      for (int j = index + 1; j < len; j++) {
        if (array[j] < min) {
          min = array[j];
          k = j;
        }
      }
      int temp = array[index];
      array[index] = array[k];
      array[k] = temp;
      index++;
    }
    return array;
  }

  public static void printArray(int[] array) {
    for (int num : array) {
      System.out.print(num + " ");
    }
    System.out.println();
  }
}
