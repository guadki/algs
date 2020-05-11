package algs.subsets

import scala.annotation.tailrec

trait Subsets {

  type Subsets[A] = List[List[A]]

  def subsets[A](list: List[A]): Subsets[A] = {
    subsetsRec(list)
  }

  @tailrec
  private def subsetsRec[A](list: List[A], acc: Subsets[A] = Nil :: Nil): Subsets[A] = {
    list match {
      case Nil => acc.map(_.reverse)
      case x :: xs => subsetsRec(xs, acc ::: acc.map(x +: _))
    }
  }


}
