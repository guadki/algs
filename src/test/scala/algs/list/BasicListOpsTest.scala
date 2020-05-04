package algs.list

import org.scalatest.funsuite.AnyFunSuite

class BasicListOpsTest extends AnyFunSuite with BasicListOps {

  test("Average of empty list should not exist ") {
    assert(avgOpt(Nil).isEmpty)
  }

  test("Average of list should be 0 ") {
    assert(avgOpt(List.fill(1000)(0)).contains(0))
  }

}
