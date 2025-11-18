// ============================================================================
// 💀 TASKLISTSKELETON - LOADING PLACEHOLDER
// ============================================================================
// Componente que exibe "fantasmas" de tarefas enquanto API carrega.
// Melhora UX mostrando estrutura da página ao invés de tela em branco.
//
// CSS Modules: estilos isolados em TaskListSkeleton.module.css
// Animação de pulse: simula carregamento com shimmer effect
//
// QUANDO USAR:
// - Primeira carga de dados da API
// - Ao invés de spinner genérico
// - Para manter layout estável (evita shift quando carrega)

import styles from './TaskListSkeleton.module.css';

/**
 * Skeleton placeholder para lista de tarefas
 * 
 * @param {number} count - Quantos skeletons exibir (padrão: 3)
 */
function TaskListSkeleton({ count = 3 }) {
  return (
    <div className={styles['skeleton-container']}>
      {/* Cria array com 'count' elementos e mapeia para skeletons */}
      {[...Array(count)].map((_, index) => (
        <div key={index} className={styles['skeleton-task']}>
          {/* Checkbox fake */}
          <div className={styles['skeleton-checkbox']}></div>
          
          {/* Conteúdo: título + badge */}
          <div className={styles['skeleton-content']}>
            <div className={styles['skeleton-title']}></div>  {/* Barra longa */}
            <div className={styles['skeleton-badge']}></div>   {/* Barra curta */}
          </div>
          
          {/* Botão deletar fake */}
          <div className={styles['skeleton-button']}></div>
        </div>
      ))}
    </div>
  );
}

export default TaskListSkeleton;
