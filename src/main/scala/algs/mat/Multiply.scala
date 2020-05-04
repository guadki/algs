package algs.mat

trait Multiply extends Transpose {

  def multiply(m1: Matrix[Int], m2: Matrix[Int]): Matrix[Int] = {
    if (m1.isEmpty || m2.isEmpty) {
      Vector.empty
    } else if (m1.forall(_.length == m1.head.length) && m1.head.length == m2.length) {
      val m2Transposed = transpose(m2)
      (for {
        l1 <- m1
        l2 <- m2Transposed
      } yield l1.lazyZip(l2).map(_ * _).sum).grouped(m1.length).toVector
    } else {
      throw new IllegalArgumentException("matrices have wrong sizes")
    }
  }

}
