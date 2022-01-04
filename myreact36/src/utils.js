
// ES6 버전의 파이썬 zip 구현
// https://stackoverflow.com/a/10284006
const zip = (...rows) => rows[0].map((_, column_index) => rows.map(row => row[column_index]));

const shuffle_array = (array) =>
    array.sort(() => Math.random() - Math.random());

export {   // import { zip, shuffle_array } from "utils";
    zip,
    shuffle_array,
};

// export default zip;  // import CCC from "utils";