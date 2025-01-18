
package Course.Course_01;

public class InsertSort {
      public static void main(String[] args) {
        int[] array = {10, 7, 8, 9, 1, 5};
        insertionSort(array);
        for(int num : array){
          System.out.print(num + " ");
        }
        System.out.println();
      }
    
          // Insertion Sort method
      public static void insertionSort(int[] array) {
        int n = array.length;
    
        for (int i = 1; i < n; i++) {
          int key = array[i]; // Current element to be inserted
          int j = i - 1;
    
          // Move elements of array[0..i-1], that are greater than key, one position ahead
          while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j]; // Shift the element to the right
            j--;
          }
          // Insert the key at the correct position
          array[j + 1] = key;
        }
      }
}

