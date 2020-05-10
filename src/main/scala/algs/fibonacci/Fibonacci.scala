package algs.fibonacci

import scala.annotation.tailrec

trait Fibonacci {

  def fib(n: Int): BigInt = {
    fibRec(n)
  }

  @tailrec
  private def fibRec(n: Int, left: BigInt = 0, right: BigInt = 1): BigInt = {
    if (n == 0) left
    else fibRec(n - 1, right, left + right)
  }

  def fibSeq(n: Int): List[BigInt] = {
    fibSeqRec(n)
  }

  @tailrec
  private def fibSeqRec(n: Int, left: BigInt = 0, right: BigInt = 1, acc: List[BigInt] = Nil): List[BigInt] = {
    if (n == 0) (left :: acc).reverse
    else fibSeqRec(n - 1, right, left + right, left :: acc)
  }

  def fibSum(n: Int): BigInt = {
    fibSumRec(n)
  }

  @tailrec
  private def fibSumRec(n: Int, left: BigInt = 0, right: BigInt = 1, acc: BigInt = 0): BigInt = {
    if (n == 0) acc + left
    else fibSumRec(n - 1, right, left + right, acc + left)
  }

}
