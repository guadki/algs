package algs

import algs.search.BinarySearch
import org.scalatest.funsuite.AnyFunSuite

class BinarySearchTest extends AnyFunSuite with BinarySearch {

  test("Search should return true when given element is in array") {
    assert(search(5, (0 to 1000).toArray))
  }

  test("Search should return false when given element is not in array") {
    assert(!search(1001, (0 to 1000).toArray))
  }

  test("Search should return false when given array is empty") {
    assert(!search(5, Array.empty))
  }

}
