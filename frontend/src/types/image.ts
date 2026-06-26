export type ImageRecord = {
  id: number;
  prompt: string;
  enhanced_prompt: string;
  style: string;
  image_url: string;
  status: string;
  created_at: string;
};

export type GeneratePayload = {
  prompt: string;
  style: string;
};
