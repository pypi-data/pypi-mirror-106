extern crate cpython;

use cpython::{PyResult, Python, py_module_initializer, py_fn};

py_module_initializer!(rusty_sieve, |py, m| {
    m.add(py, "__doc__", "Prime number sieve implemented in Rust.")?;
    m.add(py, "prime_sieve", py_fn!(py, prime_sieve(n: usize)))?;
    Ok(())
});

fn prime_sieve(_py: Python, n: usize) -> PyResult<Vec<usize>> {

    // candidates vector as bools (mutable) length = n; all values = true
    let mut candidates = vec![true; n];
    candidates[0] = false;
    candidates[1] = false;

    // limit is sqrt(n) 
    let limit = (n as f64).sqrt() as usize + 1;

    // eliminate all factors of i
    for i in 2..limit {
        if candidates[i] {
            for j in (i+i..candidates.len()).step_by(i) {
                candidates[j] = false;
            }   
        }
    }

    // need to return Ok enum with data attached.
    Ok(primes_from_bool_vec(&candidates))
}

fn primes_from_bool_vec(candidates: &Vec<bool>) -> Vec<usize> {
    // store primes 
    let mut primes: Vec<usize> = Vec::new();
    for i in 2..candidates.len() {
        if candidates[i] {
            primes.push(i);
        }
    }
    primes
}



