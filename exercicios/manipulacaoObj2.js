const order = {
  name: 'Rafael Andrade',
  phoneNumber: '11-98763-1416',
  address: {
    street: 'Rua das Flores',
    number: '389',
    apartment: '701',
  },
  order: {
    pizza: {
      marguerita: {
        amount: 1,
        price: 25,
      },
      pepperoni: {
        amount: 1,
        price: 20,
      },
    },
    drinks: {
      coke: {
        type: 'Coca-Cola Zero',
        price: 10,
        amount: 1,
      },
    },
    delivery: {
      deliveryPerson: 'Ana Silveira',
      price: 5,
    },
  },
  payment: {
    total: 60,
  },
};

const customerInfo = (fullOrder) => {
  const {
    name,
    phoneNumber,
    address: { street, number, apartment },
    order: { pizza, drinks, delivery },
  } = fullOrder;

  return `Olá, ${delivery['deliveryPerson']}, entrega para: ${name}
  Telefone: ${phoneNumber}, ${street}, Numero: ${number}, ${apartment}`
}

// console.log(customerInfo(order));

const orderModifier = (fullOrder) => {
  fullOrder['name'] = 'Luiz Silva';
  fullOrder['payment']['total'] = 50;

  return `Olá, ${fullOrder['name']}, o valor total do seu pedido de
  ${Object.keys(fullOrder.order['pizza']).join(', ')} e ${fullOrder.order['drinks']['coke'].type}
  é R$${fullOrder.payment.total},00`;
}

// console.log(orderModifier(order));
// console.log(Object.keys(order.order['pizza']).join(', '))