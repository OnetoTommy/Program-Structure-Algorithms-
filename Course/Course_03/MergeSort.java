package Course.Course_03;

public class MergeSort {
  public static void main(String[] args) {
    int[] array = new int[]{10, 7, 8, 9, 1, 5};
    System.out.println("Orginal");
    printArray(array);
    merge(array, 0, array.length-1);
    System.out.println("Merge Sort");
    printArray(array);
  }

  public static void merge(int[] array, int left, int right){
    if (left < right) {
      int mid = (right + left) / 2;

      merge(array, left, mid);
      merge(array, mid+1, right);

      mergeSort(array, left, mid, right);

    }
  }

  public static void mergeSort(int[] array, int left, int mid, int right){
    
    int n1 = mid - left + 1;
    int n2 = right - mid;

    int[] leftArray = new int[n1];
    int[] rightArray = new int[n2];

    for(int i = 0; i < n1; i++){
      leftArray[i] = array[left + i];
    }
    for(int i = 0; i < n2; i++){
      rightArray[i] = array[mid + i + 1];
    }

    int i = 0, j = 0;
    int k = left;

    while (i < n1 && j < n2) {
      if (leftArray[i] >= rightArray[j]) {
        array[k] = rightArray[j];
        j++;
      }else{
        array[k] = leftArray[i];
        i++;
      }
      k++;
    }

    while (i < n1) {
      array[k] = leftArray[i];
      i++;
      k++;
    }

    while (j < n2) {
      array[k] = rightArray[j];
      j++;
      k++;
    }




  }

  public static void printArray(int[] array){
    for (int num : array){
      System.out.print(num + " ");
    }
    System.out.println();
  }
  
  
}
