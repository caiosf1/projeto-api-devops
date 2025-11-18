import styles from './TaskListSkeleton.module.css';

/**
 * Skeleton placeholder para lista de tarefas
 * Melhora UX mostrando "fantasmas" enquanto carrega
 */
function TaskListSkeleton({ count = 3 }) {
  return (
    <div className={styles['skeleton-container']}>
      {[...Array(count)].map((_, index) => (
        <div key={index} className={styles['skeleton-task']}>
          <div className={styles['skeleton-checkbox']}></div>
          <div className={styles['skeleton-content']}>
            <div className={styles['skeleton-title']}></div>
            <div className={styles['skeleton-badge']}></div>
          </div>
          <div className={styles['skeleton-button']}></div>
        </div>
      ))}
    </div>
  );
}

export default TaskListSkeleton;
