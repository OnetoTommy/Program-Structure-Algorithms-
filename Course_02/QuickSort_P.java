

public class QuickSort_P {
  public static void main(String[] args) {
    int[] array = {10, 7, 8, 9, 1, 5};
    QuickSort_P qs = new QuickSort_P();
    System.out.println("Orginal");
    qs.printArray(array);
    System.out.println("Sort");
    int len = array.length;
    qs.sortArray(array, 0, len-1);
    qs.printArray(array);

  }

  public void sortArray(int[] array, int start, int end){
    if (start < end) {
      int pivot = pivotValue(array, start, end);
      sortArray(array, start, pivot-1);
      sortArray(array, pivot+1, end);
    }
  }

  public int pivotValue(int[] array, int start, int end){
    int i = start - 1;
    int pivot = array[end];
    for(int j = start; j < end; j++){
      if(array[j] <= pivot){
        i++;
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
    int temp = array[i+1];
    array[i+1] = array[end];
    array[end] = temp;
    int result= i + 1;
    return result;
  }



  public void printArray(int[] array){
    for (int num : array){
      System.out.print(num + " ");
    }
    System.out.println();
  }
}
