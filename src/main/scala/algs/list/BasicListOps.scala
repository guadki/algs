package algs.list

import scala.annotation.tailrec

trait BasicListOps {

  def maxOpt(list: List[Int]): Option[Int] = {
    if (list.isEmpty)
      None
    else
      Some(list.reduce((x, y) => if (x >= y) x else y))
  }

  def minOpt(list: List[Int]): Option[Int] = {
    if (list.isEmpty)
      None
    else
      Some(list.reduce((x, y) => if (x <= y) x else y))
  }

  def avgOpt(list: List[Int]): Option[Double] = {
    if (list.isEmpty)
      None
    else
      Some(list.map(_.toDouble).sum / list.length)
  }

  def reverse[A](list: List[A]): List[A] = {
    reverseRec(list)
  }

  @tailrec
  private def reverseRec[A](list: List[A], acc: List[A] = Nil): List[A] = {
    list match {
      case Nil => acc
      case x :: xs => reverseRec(xs, x :: acc)
    }
  }

  def isSorted(list: List[Int]): Boolean = {
    isSortedRec(list)
  }

  @tailrec
  private def isSortedRec(list: List[Int], acc: Boolean = true): Boolean = {
    if (acc) {
      list match {
        case Nil => acc
        case _ :: Nil => isSortedRec(Nil, acc)
        case x :: xs => isSortedRec(xs, acc && (x <= xs.head))
      }
    } else {
      acc
    }
  }

}
