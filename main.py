import random
import numpy as np

w = 0.9
c1 = .3
c2 = .5
dimension = 3
iterations = 100
n_particles = 20


class Particle:
    def __init__(self):
        self.v = []
        self.s = []
        self.pBest = []
        for i in range(dimension):
            self.s.append(random.random())
            self.v.append(random.random())
            self.pBest.append(self.s[i])

    def update_s(self):
        for i in range(dimension):
            self.s[i] = self.s[i] + self.v[i]

    def update_v(self, gBest):
        for i in range(dimension):
            r1 = random.random()
            r2 = random.random()
            g_best = c1 * r1 * (gBest[i] - self.s[i])
            p_best = c2 * r2 * (self.pBest[i] - self.s[i])
            self.v[i] = (w * self.v[i]) + g_best + p_best


class ParticleSwarmOptimizer:
    def __init__(self):
        self.particles = []
        for h in range(n_particles):
            particle = Particle()
            self.particles.append(particle)

    def optimize(self):
        for i in range(iterations):
            #gbest
            gBest = self.particles[0].pBest
            for j in range(n_particles):
                pBest = self.particles[j].pBest
                if self.f(pBest) > self.f(gBest):
                    gBest = pBest
            #update all
            for k in range(n_particles):
                self.particles[k].update_v(gBest)
                self.particles[k].update_s()
            #update all pbest
            for l in range(n_particles):
                pBest = self.particles[l].pBest
                if l ==10:
                    print(self.particles[l].s)
                if self.f(self.particles[l].s) > self.f(self.particles[l].pBest):
                    self.particles[l].pBest = self.particles[l].s
        return gBest

    def f(self, tmp):
        tmp = np.array(tmp)
        tmp = tmp.reshape(1,-1)
        return (tmp ** 2).sum(axis=1)


def main():
    pso = ParticleSwarmOptimizer()
    solution = pso.optimize()
    print(solution)


if __name__ == '__main__':
    main()
