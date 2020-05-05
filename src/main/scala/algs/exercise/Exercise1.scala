package algs.exercise

/*
  Write a program, which will index each letter in a text to words.
  Program does not have to take letter case into consideration.
  Words that occur many times in a text must be presented only once in output.
  List of words in which particular letter occurs, should be sorted alphabetically.
*/

trait Exercise1 {
  type Index = Seq[(Char, Set[String])]

  private def sortedLetters(input: String): Seq[Char] = {
    input
      .map(_.toLower)
      .filter((a: Char) => a.isLetter)
      .toSet
      .toSeq
      .sorted
  }

  private def uniqueWords(input: String): Set[String] = {
    input
      .map(_.toLower)
      .filter((a: Char) => a.isLetter || a.isSpaceChar)
      .split(' ')
      .toSet
  }

  def indexWords(input: String): Index = {
    val words: Set[String] = uniqueWords(input)

    sortedLetters(input)
      .map(letter => (letter, words.filter(_.contains(letter))))
  }


  def printIndex(index: Index): Unit = {
    index.foreach { case (c, words) => println(s"$c: ${words.mkString(", ")}") }
  }

}
