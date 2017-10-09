# WIP State
State wip_state
State desired_state
State fdbk_state

# Equilibrium condition:
float32 u_eq_left
float32 u_eq_right
float32 phi_eq

# Current actuation:
float32 u_left
float32 u_right

# Current wheel velocity:
float32 w_left
float32 w_right

# IMU sensed:
float32 roll
float32 pitch

# Sensed floor:
float32 ramp_psi
float32 ramp_delta

