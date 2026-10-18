package utils

import (
	"strings"
	"unicode"
)

func squashSpaces(value string) string {
	return strings.Join(strings.Fields(value), " ")
}

func NormalizeName(name string) string {
	words := strings.Fields(strings.ToLower(squashSpaces(name)))
	for i, word := range words {
		runes := []rune(word)
		runes[0] = unicode.ToUpper(runes[0])
		words[i] = string(runes)
	}
	return strings.Join(words, " ")
}
