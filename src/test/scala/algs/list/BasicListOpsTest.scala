package algs.list

import org.scalatest.funsuite.AnyFunSuite

import scala.util.Random

class BasicListOpsTest extends AnyFunSuite with BasicListOps {

  test("Average of empty list should not exist ") {
    assert(avgOpt(Nil).isEmpty)
  }

  test("Average of list should be 0 ") {
    assert(avgOpt(List.fill(1000)(0)).contains(0))
  }

  test("Sorted list should return true") {
    assert(isSorted(List(0, 2, 6, 8, 12, 125, 123214, 1214124)))
  }

  test("Not sorted list should return false") {
    assert(!isSorted(List(0, 2, 1, 8, 12, 125, 123214, 1214124)))
  }

  test("isSorted should work for large inputs") {
    val r = new Random()
    assert(!isSorted((0 to 1000000).map(_ => r.nextInt()).toList))
  }

}
