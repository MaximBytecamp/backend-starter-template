package services

import (
	"errors"
	"math"
	"slices"
)

var ErrNoGrades = errors.New("список оценок пуст")

func CalculateAverage(grades []int) (float64, error) {
	if len(grades) == 0 {
		return 0, ErrNoGrades
	}
	sum := 0
	for _, grade := range grades {
		sum += grade
	}
	// Сумма переводится в float64 до деления: деление двух int
	// отбросило бы дробную часть, и среднее 4.4 стало бы 4.
	return math.Round(sum/len(grades)*100) / 100, nil
}

func GradeBounds(grades []int) (low, high int, err error) {
	if len(grades) == 0 {
		return 0, 0, ErrNoGrades
	}
	return slices.Min(grades), slices.Max(grades)
}
