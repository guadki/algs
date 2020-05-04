package algs.gcd

import algs.gcd.GCD
import org.scalatest.funsuite.AnyFunSuite

class GCDTest extends AnyFunSuite with GCD {

  test("Greatest common divider of 10 and 20 should be 10") {
    assert(greatestCommonDivider(10, 20) == 10)
  }

  test("Greatest common divider of -5 and 20 should be -5") {
    assert(greatestCommonDivider(-5, 20) == -5)
  }

  test("Greatest common divider of -5 and -20 should be -5") {
    assert(greatestCommonDivider(-5, -20) == -5)
  }

  test("Greatest common divider of 10 and -20 should be 10") {
    assert(greatestCommonDivider(10, -20) == 10)
  }

  test("Greatest common divider of 0 and -1 should be -1") {
    assert(greatestCommonDivider(0, -1) == -1)
  }

  test("Greatest common divider of -1 and 0 should be -1") {
    assert(greatestCommonDivider(-1, 0) == -1)
  }

}
