package algs.gcd

import org.scalacheck.Prop.forAll
import org.scalacheck.Properties

object GCDPropTest extends Properties("GcdTest") with GCD {

  property("Result should be a divider for both params") = forAll { (x1: Int, x2: Int) =>
    val gcd = greatestCommonDivider(x1, x2)
    gcd == 0 || (x1 % gcd == 0 && x2 % gcd == 0)
  }
}
