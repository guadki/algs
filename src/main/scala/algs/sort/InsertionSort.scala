package algs.sort

trait InsertionSort {

  def sort(array: Array[Int]): Array[Int] = {
    for (i <- 1 until array.length) {
      val key = array(i)
      var j = i - 1

      while (j >= 0 && array(j) > key) {
        array(j + 1) = array(j)
        j = j - 1
      }

      array(j + 1) = key
    }
    array
  }

}
