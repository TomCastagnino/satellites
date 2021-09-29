
export const parseResources = (resources) => {
    const intArray = resources.split(',').map(num => parseInt(num));
    return intArray;
};
