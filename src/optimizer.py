import numpy as np
import pygad

NUM_PERSONAS = 7
MAX_TURNOS_POR_PERSONA = 6
TOTAL_TURNOS = 14  # 2 diarios por 7 días
PERSONAS_POR_TURNO = 3
TOTAL_GENES = TOTAL_TURNOS * PERSONAS_POR_TURNO  # 42 genes

def fitness_func(ga_instance, solution, solution_idx):
    horario = np.round(solution).astype(int)
    
    violaciones_turno = 0
    conteo_turnos_persona = np.zeros(NUM_PERSONAS, dtype=int)
    
    # 1. Validar restricciones por turno
    for i in range(TOTAL_TURNOS):
        turno = horario[i * PERSONAS_POR_TURNO : (i + 1) * PERSONAS_POR_TURNO]
        if len(np.unique(turno)) < PERSONAS_POR_TURNO:
            violaciones_turno += (PERSONAS_POR_TURNO - len(np.unique(turno)))
            
        for persona in turno:
            if 0 <= persona < NUM_PERSONAS:
                conteo_turnos_persona[persona] += 1

    # 2. Validar restricciones de exceso (máximo 6 turnos)
    violaciones_exceso = 0
    for conteo in conteo_turnos_persona:
        if conteo > MAX_TURNOS_POR_PERSONA:
            violaciones_exceso += (conteo - MAX_TURNOS_POR_PERSONA)
            
    total_violaciones = violaciones_turno + violaciones_exceso
    return -1.0 * total_violaciones

def ejecutar_optimizacion():
    """Ejecuta el algoritmo genético y retorna el mejor horario encontrado."""
    gene_space = [list(range(NUM_PERSONAS)) for _ in range(TOTAL_GENES)]

    ga_instance = pygad.GA(
        num_generations=100,
        num_parents_mating=10,
        fitness_func=fitness_func,
        sol_per_pop=50,
        num_genes=TOTAL_GENES,
        gene_space=gene_space,
        mutation_percent_genes=2,
        gene_type=int
    )

    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    
    return {
        "fitness": float(solution_fitness),
        "horario": np.round(solution).astype(int).tolist()
    }