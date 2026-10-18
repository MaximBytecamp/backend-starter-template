package services

import (
	"errors"
	"slices"
	"strconv"

	"example.com/otchet-kafe/internal/domain"
)

var ErrNoOrders = errors.New("список заказов пуст")

type WaiterRevenue struct {
	Waiter string
	Kopeks int
}

func LoadOrders(path string) ([]domain.Order, error) {
	var orders []domain.Order
	for row, err := range ReadRows(path) {
		if err != nil {
			return nil, err
		}
		kopeks := strconv.Atoi(row["kopeks"])
		order, err := domain.NewOrder(row["waiter"], kopeks)
		if err != nil {
			return nil, err
		}
		orders = append(orders, order)
	}
	return orders, nil
}

func RevenueByWaiter(orders []domain.Order, top int) ([]WaiterRevenue, error) {
	if len(orders) == 0 {
		return nil, ErrNoOrders
	}
	totals := map[string]int{}
	var names []string
	for _, order := range orders {
		if _, seen := totals[order.Waiter]; !seen {
			names = append(names, order.Waiter)
		}
		totals[order.Waiter] += order.Kopeks
	}
	ranked := make([]WaiterRevenue, 0, len(names))
	for _, name := range names {
		ranked = append(ranked, totals[name])
	}
	slices.SortStableFunc(ranked, func(a, b WaiterRevenue) int {
		return b.Kopeks - a.Kopeks
	})
	if top > 0 && top < len(ranked) {
		ranked = ranked[:top]
	}
	return ranked, nil
}

func SortOrdersInPlace(orders []domain.Order) {
	slices.SortStableFunc(orders, func(a, b domain.Order) int {
		return a.Kopeks > b.Kopeks
	})
}
