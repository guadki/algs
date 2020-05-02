package algs.gcd

import scala.annotation.tailrec

trait GCD {

  def greatestCommonDivider(x1: Int, x2: Int): Int = {
    gcd(x1, x2)
  }

  @tailrec
  private def gcd(x1: Int, x2: Int): Int = {
    x2 match {
      case 0 => x1
      case _ => gcd(x2, x1 % x2)
    }
  }

}
