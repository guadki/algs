package algs.mat

import scala.annotation.tailrec

trait Transpose {

  def transpose[A](mat: Matrix[A]): Matrix[A] = {
    if (mat.forall(_.length == mat.head.length)) {
      transposeRec(mat)
    } else throw new IllegalArgumentException("transpose requires all collections have the same size")
  }

  @tailrec
  private def transposeRec[A](mat: Matrix[A], acc: Matrix[A] = Vector.empty): Matrix[A] = {
    mat.filter(_.nonEmpty) match {
      case Vector() => acc
      case mat: Matrix[A] => transposeRec(mat.map(_.tail), acc :+ mat.map(_.head))
    }
  }

}
