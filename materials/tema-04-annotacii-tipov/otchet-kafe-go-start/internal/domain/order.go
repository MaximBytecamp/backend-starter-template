package domain

import (
	"errors"

	"example.com/otchet-kafe/internal/utils"
)

var ErrNegativeKopeks = errors.New("сумма заказа не может быть отрицательной")

type Order struct {
	Waiter string
	Kopeks int
}

func NewOrder(waiter string, kopeks int) (Order, error) {
	if kopeks < 0 {
		return Order{}, ErrNegativeKopeks
	}
	return Order{Waiter: utils.NormalizeName(waiter), Kopeks: kopeks}, nil
}
