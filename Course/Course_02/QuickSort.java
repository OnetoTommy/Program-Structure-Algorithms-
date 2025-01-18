public class QuickSort {
  // Main method to test the QuickSort
  public static void main(String[] args) {
      int[] array = {10, 7, 8, 9, 1, 5};
      System.out.println("Original Array:");
      printArray(array);

      quickSort(array, 0, array.length - 1);

      System.out.println("Sorted Array:");
      printArray(array);
  }

  // QuickSort method
  public static void quickSort(int[] array, int low, int high) {
      if (low < high) {
          // Partition the array and get the pivot index
          int pi = partition(array, low, high);

          // Recursively sort elements before and after the pivot
          quickSort(array, low, pi - 1);  // Left side of the pivot
          quickSort(array, pi + 1, high); // Right side of the pivot
      }
  }

  // Partition method to place the pivot in its correct position
  public static int partition(int[] array, int low, int high) {
      int pivot = array[high];  // Choose the last element as the pivot
      int i = low - 1;          // Index of the smaller element

      for (int j = low; j < high; j++) {
          // If the current element is smaller than or equal to the pivot
          if (array[j] <= pivot) {
              i++;
              // Swap array[i] and array[j]
              int temp = array[i];
              array[i] = array[j];
              array[j] = temp;
          }
      }

      // Swap the pivot element with the element at index (i + 1)
      int temp = array[i + 1];
      array[i + 1] = array[high];
      array[high] = temp;

      return i + 1;  // Return the index of the pivot
  }

  // Utility method to print an array
  public static void printArray(int[] array) {
      for (int num : array) {
          System.out.print(num + " ");
      }
      System.out.println();
  }
}
