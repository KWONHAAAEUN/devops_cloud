import { useState } from 'react';

function useFieldValues(initialFieldVlaues) {
  const [fieldValues, setFieldValues] = useState(initialFieldVlaues);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFieldValues((prevFieldValures) => {
      return {
        ...prevFieldValures,
        [name]: value,
      };
    });
  };
  return [fieldValues, handleChange];
}

export default useFieldValues;
