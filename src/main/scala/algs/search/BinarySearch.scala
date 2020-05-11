package algs.search

import scala.annotation.tailrec

trait BinarySearch {

  def search(elem: Int, arr: Array[Int]): Boolean = {
    bin(elem, arr, 0, arr.length - 1)
  }

  @tailrec
  private def bin(elem: Int, arr: Array[Int], start: Int, end: Int): Boolean = {
    if (start > end) false
    else {
      val mid = start + (end - start) / 2
      val current = arr(mid)
      if (current == elem) true
      else if (current < elem) bin(elem, arr, mid + 1, end)
      else bin(elem, arr, start, mid - 1)
    }
  }

}
