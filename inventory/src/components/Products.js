import React, { useState, useEffect } from 'react';

const Products = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch products from API
    setProducts([
      { id: 1, name: 'Router', stock: 10 },
      { id: 2, name: 'Switch', stock: 5 },
    ]);
  }, []);

  return (
    <div>
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - Stock: {product.stock}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Products;
