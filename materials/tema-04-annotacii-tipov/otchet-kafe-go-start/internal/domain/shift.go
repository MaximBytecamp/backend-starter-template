package domain

import "time"

type Shift struct {
	Day    time.Time
	Orders []Order
}

func NewShift(day time.Time) *Shift {
	return &Shift{Day: day}
}

func (s *Shift) Add(order Order) {
	s.Orders = append(s.Orders, order)
}

func (s *Shift) TotalKopeks() int {
	total := 0
	for _, order := range s.Orders {
		total += order.Kopeks
	}
	return total
}
