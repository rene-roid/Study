// "Catch"

// Try-catch / finally

try {
    // First this code runs until it finds a error
    console.log(test);
} catch (error) {
    // If there is a error this code is ran
    console.error();
    console.log(error.message);
} finally {
    // This is always ran
    console.log('Finally was ran n\ LES GOOOOOO')
}