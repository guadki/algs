package algs.mss

/*
  Given an array of n numbers, calculate the maximum subarray sum,
  i.e., the largest possible sum of a sequence of consecutive values
  in the array.
 */

trait MaxSubarraySum {

  def maxSubarraySum(input: Array[Int]): Int = {
    var best, sum = 0
    for (k <- input.indices) {
      sum = Math.max(input(k), sum + input(k))
      best = Math.max(best, sum)
    }
    best
  }

  def mss(list: List[Int]): Int = {
    mssRec(list)
  }

  @scala.annotation.tailrec
  private def mssRec(xs: List[Int], sum: Int = 0, best: Int = 0): Int = {
    xs match {
      case Nil => Math.max(best, sum)
      case x :: xs => mssRec(xs, Math.max(x, sum + x), Math.max(best, sum))
    }
  }

}
