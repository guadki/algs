package algs.sort

import scala.annotation.tailrec

trait MergeSort {

  def sort(list: List[Int]): List[Int] = {
    val mid = list.length / 2
    mid match {
      case 0 => list
      case _ =>
        val (left, right) = list.splitAt(mid)
        merge(sort(left), sort(right))
    }
  }

  /*
    Note: `acc.reverse ::: left` and `lHead :: acc` is much
    cheaper than `acc ::: left` and `acc :+ lHead`
 */
  @tailrec
  private def merge(left: List[Int], right: List[Int], acc: List[Int] = Nil): List[Int] = {
    (left, right) match {
      case (_, Nil) => acc.reverse ::: left
      case (Nil, _) => acc.reverse ::: right
      case (lHead :: lTail, rHead :: rTail) =>
        if (lHead < rHead) merge(lTail, right, lHead :: acc)
        else merge(left, rTail, rHead :: acc)
    }
  }

}
