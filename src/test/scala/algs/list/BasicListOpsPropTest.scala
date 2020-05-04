package algs.list

import org.scalacheck.Prop.forAll
import org.scalacheck.Properties

object BasicListOpsPropTest extends Properties("BasicListOpsTest") with BasicListOps {

  property("result should be max from list elements") = forAll { input: List[Int] =>
    maxOpt(input) == input.maxOption
  }

  property("result should be min from list elements") = forAll { input: List[Int] =>
    minOpt(input) == input.minOption
  }

  property("result should be reversed input list") = forAll { input: List[Int] =>
    reverse(input) == input.reverse
  }

}
