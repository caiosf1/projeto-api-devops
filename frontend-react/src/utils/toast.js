import { toast } from 'react-toastify';

/**
 * Utilitário para notificações toast
 * Wrapper para react-toastify com configurações padrão
 */

const defaultConfig = {
  position: 'top-right',
  autoClose: 3000,
  hideProgressBar: false,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
};

export const notify = {
  success: (message) => toast.success(message, defaultConfig),
  error: (message) => toast.error(message, defaultConfig),
  info: (message) => toast.info(message, defaultConfig),
  warning: (message) => toast.warning(message, defaultConfig),
};
